.. _based_features:

Based Features
==============


Intersection Types
------------------

Using the ``&`` operator or ``basedtyping.Intersection`` you can denote intersection types:

.. code-block:: python

    class Growable(ABC, Generic[T]):
        @abstractmethod
        def add(self, item: T): ...


    class Resettable(ABC):
        @abstractmethod
        def reset(self): ...


    def f(x: Resettable & Growable[str]):
        x.reset()
        x.add("first")

Type Joins
----------

Mypy joins types to their common base type:

.. code-block:: python

    a: int
    b: str
    reveal_type(a if bool() else b)  # Revealed type is "builtins.object"

Basedmypy joins types into unions instead:

.. code-block:: python

    a: int
    b: str
    reveal_type(a if bool() else b)  # Revealed type is "int | str"

Bare Literals
-------------

``Literal`` is so cumbersome! Just use a bare literal instead:

.. code-block:: python

    class Color(Enum):
        RED = auto()

    a: 1 | 2
    b: True | Color.RED


Default Return Type
-------------------

The default return type of functions is ``None`` instead of ``Any``:
(configurable with the :confval:`default_return` option.)

.. code-block:: python

    def f(name: str):
        print(f"Hello, {name}!")

    reveal_type(f)  # (str) -> None

Generic ``TypeVar`` Bounds
--------------------------

Basedmpy allows the bounds of ``TypeVar``\s to be generic.

So you are able to have functions with polymorphic generic parameters:

.. code-block:: python

    E = TypeVar("E")
    I = TypeVar("I", bound=Iterable[E])


    def foo(i: I, e: E) -> I:
        assert e not in i
        return i


    reveal_type(foo(["based"], "mypy"))  # N: Revealed type is "list[str]"
    reveal_type(foo({1, 2}, 3))  # N: Revealed type is "set[int]"

Reinvented type guards
----------------------

``TypeGuard`` acts similar to ``cast``, which is often sub-optimal and dangerous:

.. code-block:: python

    def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
        return all(isinstance(x, str) for x in val)

    l1: list[object] = []
    l2 = l1

    if is_str_list(l1):
        l2.append(100)
        reveal_type(l1[0])  # Revealed type is "str", at runtime it is 100


    class A: ...
    class B(A): ...
    def is_a(val: object) -> TypeGuard[A]: ...

    b = B()
    if is_a(b):
        reveal_type(b)  # A, not B


Basedmypy introduces a simpler and more powerful denotation for type-guards, and changes their behavior
to be safer.

.. code-block:: python

    def is_int(value: object) -> value is int: ...

Type-guards don't widen:

.. code-block:: python

    a: bool
    if is_int(a):
        reveal_type(a)  # Revealed type is "bool"

Type-guards work on the implicit ``self`` and ``cls`` parameters:

.. code-block:: python

    class A:
        def guard(self) -> self is B: ...
    class B(A): ...

    a = A()
    if a.guard():
        reveal_type(a)  # Revealed type is "B"

Invalid type-guards show an error:

.. code-block:: python

    def guard(x: str) -> x is int: # error: A type-guard's type must be assignable to its parameter's type.

If you want to achieve something similar to the old ``TypeGuard``:

.. code-block:: python

    def as_str_list(val: list[object]) -> list[str] | None:
        return (
            cast(list[str], val)
            if all(isinstance(x, str) for x in val)
            else None
        )

    a: list[object]
    if (str_a := as_str_list(a)) is not None:
        ...

    # or

    def is_str_list(val: list[object]) -> bool:
        return all(isinstance(x, str) for x in val)

    a: list[object]
    if is_str_list(a):
        str_a = cast(list[str], a)
        ...

Overload Implementation Inference
---------------------------------

The types in overload implementations (including properties) can be inferred:

.. code-block:: python

    @overload
    def f(a: int) -> str: ...

    @overload
    def f(a: str) -> int: ...

    def f(a):
        reveal_type(a)  # int | str
        return None  # error: expected str | int

    class A:
        @property
        def foo(self) -> int: ...
        @foo.setter
        def foo(self, value): ...  # no need for annotations


Infer Function Parameters
-------------------------

Infer the type of a function parameter from its default value:

.. code-block:: python

    def f(a=1, b=True):
        reveal_type((a, b))  # (int, bool)

Covariant Mapping key type
--------------------------

The key type of ``Mapping`` is fixed to be covariant:

.. code-block:: python

    a: Mapping[str, str]
    b: Mapping[object, object] = a  # no error

Tuple Literal Types
-------------------

Basedmypy allows denotation of tuple types with tuple literals:

.. code-block:: python

    a: (int, str) = (1, "a")

Types in Messages
-----------------

Basedmypy makes significant changes to error and info messages, consider:

.. code-block:: python

    T = TypeVar("T", bound=int)

    def f(a: T, b: list[str | 1 | 2]) -> Never:
        reveal_type((a, b))

    reveal_type(f)

Mypy shows::

    Revealed type is "Tuple[T`-1, Union[builtins.str, Literal[1], Literal[2]]]"
    Revealed type is "def [T <: builtins.int] (a: T`-1, b: Union[builtins.str, Literal[1], Literal[2]]) -> <nothing>"

Basedmypy shows::

    Revealed type is "(T@f, str | 1 | 2)"
    Revealed type is "def [T: int] (a: T, b: str | 1 | 2) -> Never"
