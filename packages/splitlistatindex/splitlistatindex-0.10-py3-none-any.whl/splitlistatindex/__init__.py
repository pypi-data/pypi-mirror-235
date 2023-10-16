def list_split(l, indices_or_sections):
    r"""
    Splits a list `l` into sublists based on either a list of indices or a number of sections.

    Args:
        l (List[T]): The input list to be split.
        indices_or_sections (Union[int, List[int]]): Either an integer representing the number of
            sections to split `l` into or a list of indices where `l` will be split. If it's an
            integer, it must be greater than 0. If it's a list, it should contain indices where
            `l` will be split.

    Returns:
        List[List[T]]: A list of sublists containing the elements of the input list `l` split
            according to the provided indices or sections. Each sublist is a segment of the
            original list `l`.

    Raises:
        ValueError: If `indices_or_sections` is an integer and is not greater than 0.
        IndexError: If any of the indices in the `indices_or_sections` list are out of bounds.

    Example:
        from splitlistatindex import list_split
        l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        l2 = [3, 5, 7, 8, 12]

        # Split `l1` using a list of indices
        result1 = list_split(l=l1, indices_or_sections=l2)
        # result1 will be: [[0, 1, 2], [3, 4], [5, 6], [7], [8, 9]]

        # Split `l1` into 3 sections
        result2 = list_split(l=l1, indices_or_sections=3)
        # result2 will be: [[0, 1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    Ntotal = len(l)
    try:
        Nsections = len(indices_or_sections) + 1
        div_points = [0] + list(indices_or_sections) + [Ntotal]
    except TypeError:
        Nsections = int(indices_or_sections)
        if Nsections <= 0:
            raise ValueError("number sections must be larger than 0.") from None
        Neach_section, extras = divmod(Ntotal, Nsections)
        section_sizes = (
            [0] + extras * [Neach_section + 1] + (Nsections - extras) * [Neach_section]
        )
        div_points = []
        new_sum = 0
        for i in section_sizes:
            new_sum += i
            div_points.append(new_sum)

    sub_arys = []
    lenar = len(l)
    for i in range(Nsections):
        st = div_points[i]
        end = div_points[i + 1]
        if st >= lenar:
            break
        sub_arys.append((l[st:end]))

    return sub_arys

