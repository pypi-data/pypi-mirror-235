from copy import deepcopy

class FFIter:
    """
    Custom Forward-Backward Iterator with Exception Handling.

    This class provides an iterator that can traverse an iterable in a forward direction,
    while keeping track of previously visited elements. It also allows for moving backward
    in the iterable, even for dictionaries, and provides options for handling exceptions
    and replacement values.

    Args:
        iterable (Iterable): The input iterable to be traversed, which can be a list or a dictionary.
        ignore_exceptions (bool, optional): If True, exceptions encountered during traversal are ignored,
            and the specified `exception_replacement` value is returned instead. Default is False.
        exception_replacement (Any, optional): The value to return when an exception occurs during
            traversal and `ignore_exceptions` is set to True. Default is None.

    Attributes:
        iterable (list): A list representation of the input iterable for efficient traversal.
        alreadydone (list): A list to keep track of elements that have already been traversed.
        still2do (list): A list of remaining elements to be traversed.
        ignore_exceptions (bool): Flag indicating whether exceptions should be ignored.
        exception_replacement (Any): The value to return when an exception occurs.
        active_index: index of active value (like enumerate)

    Methods:
        __iter__(): Return an iterator for the iterable, supporting forward traversal.
        forward(n=1): Retrieve the element n positions forward in the iterable.
        back(n): Retrieve the element n positions backward in the iterable.

    Example Usage:
        from loophopper import FFIter
        # Create an FFIter object for a range iterable
        l = FFIter(range(40), ignore_exceptions=True, exception_replacement=None)
        for no in l:
            if no % 10 == 0:
                print(f"number: {no}, 2 forward: {l.forward(2)}")
            if no % 7 == 0:
                print(f"number: {no}, 1 back: {l.back(1)}")

        # Create an FFIter object for a dictionary iterable
        l = FFIter(
            {k: k * 2 for k in range(40)}, ignore_exceptions=True, exception_replacement=None
        )
        for no in l:
            if no[0] % 10 == 0:
                print(f"number: {no}, 2 forward: {l.forward(2)}")
            if no[1] % 7 == 0:
                print(f"number: {no}, 1 back: {l.back(1)}")

        l = FFIter(
            {k: k * 2 for k in range(40)}, ignore_exceptions=True, exception_replacement=None
        )
        for no in l:
            if l.active_index%5==0:
                print(f'{l.active_index}: {no}')

        # number: 0, 2 forward: 2
        # number: 0, 1 back: None
        # number: 7, 1 back: 6
        # number: 10, 2 forward: 12
        # number: 14, 1 back: 13
        # number: 20, 2 forward: 22
        # number: 21, 1 back: 20
        # number: 28, 1 back: 27
        # number: 30, 2 forward: 32
        # number: 35, 1 back: 34
        # number: (0, 0), 2 forward: (2, 4)
        # number: (0, 0), 1 back: None
        # number: (7, 14), 1 back: (6, 12)
        # number: (10, 20), 2 forward: (12, 24)
        # number: (14, 28), 1 back: (13, 26)
        # number: (20, 40), 2 forward: (22, 44)
        # number: (21, 42), 1 back: (20, 40)
        # number: (28, 56), 1 back: (27, 54)
        # number: (30, 60), 2 forward: (32, 64)
        # number: (35, 70), 1 back: (34, 68)
        # 0: (0, 0)
        # 5: (5, 10)
        # 10: (10, 20)
        # 15: (15, 30)
        # 20: (20, 40)
        # 25: (25, 50)
        # 30: (30, 60)
        # 35: (35, 70)
    """
    def __init__(self, iterable, ignore_exceptions=False, exception_replacement=None):
        if isinstance(iterable, dict):
            self.iterable = list(iterable.items())
        else:
            self.iterable = list(iterable)
        self.alreadydone = []
        try:
            self.still2do = deepcopy(self.iterable)
        except Exception:
            self.still2do = self.iterable

        self.ignore_exceptions = ignore_exceptions
        self.exception_replacement = exception_replacement
        self.active_index = 0

    def __iter__(self):
        """
        Returns an iterator for the iterable, supporting forward traversal.
        """
        for ini,i in enumerate(self.iterable):
            self.alreadydone.append(i)
            self.still2do.pop(0)
            self.active_index = ini
            yield i

    def forward(self, n=1):
        """
        Retrieve the element n positions forward in the iterable.

        Args:
            n (int, optional): Number of positions to move forward. Default is 1.

        Returns:
            Any: The element found n positions forward, or the specified
                 `exception_replacement` value in case of exceptions.
        """
        try:
            return self.still2do[n - 1]
        except Exception as e:
            if self.ignore_exceptions:
                return self.exception_replacement
            else:
                raise e

    def back(self, n):
        """
        Retrieve the element n positions backward in the iterable.

        Args:
            n (int): Number of positions to move backward.

        Returns:
            Any: The element found n positions backward, or the specified
                 `exception_replacement` value in case of exceptions.
        """
        try:
            return self.alreadydone[-n - 1]
        except Exception as e:
            if self.ignore_exceptions:
                return self.exception_replacement
            else:
                raise e
