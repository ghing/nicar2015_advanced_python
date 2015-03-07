from pycar_advanced.results import Result

def generate_results(results_list):
    """
    Generate an iterator of Result objects from a list of dictionary
    containing result attributes

    Args:
        results_list: An iterable of dictionaries representing election
            results.  Each dictionary should have at least the following
            keys: `candidate_name`, `candidate_id`, and `total_votes`.

    Returns:
        An iterator over Result objects created from the attributes in
        results_list

    """
    # TODO: Implement this generator 
    for result_dict in results_list:
        yield Result(
            candidate_name=result_dict['candidate_name'],
            candidate_id=result_dict['candidate_id'],
            total_votes=int(result_dict['total_votes'])
        )

def candidate_first_names(results):
    """
    Return a list of candidate first names from an iterable of Result
    objects.

    Args:
        results: Iterable of Result objects

    Returns:
        List of candidate first names from Result objects

    """
    # TODO: Use a list comprehension to generate a list of candidate first
    # names from an iterable of Result objects
    return [r.candidate_name.split(' ')[0] for r in results]
