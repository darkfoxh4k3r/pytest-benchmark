def pytest_benchmark_generate_machine_info(config):
    pass


def pytest_benchmark_update_machine_info(config, info):
    """
    If benchmarks are compared and machine_info is different then warnings will be shown.

    To add the current user to the commit info override the hook in your conftest.py like this:

    .. sourcecode:: python

        def pytest_benchmark_update_machine_info(info):
            info['user'] = getpass.getuser()

    Or to completely replace the dict:

    .. sourcecode:: python

        def pytest_benchmark_update_machine_info(info):
            info.clear()
            info['user'] = getpass.getuser()
    """
    pass


def pytest_benchmark_generate_commit_info(config):
    pass


def pytest_benchmark_update_commit_info(config, info):
    pass


def pytest_benchmark_group_stats(config, benchmarks, group_by):
    pass


def pytest_benchmark_generate_json(config, benchmarks, include_data):
    pass


def pytest_benchmark_update_json(config, benchmarks, output_json):
    pass


def pytest_benchmark_compare_machine_info(config, benchmarksession, machine_info, compared_benchmark):
    pass


pytest_benchmark_generate_commit_info.firstresult = True
pytest_benchmark_generate_json.firstresult = True
pytest_benchmark_generate_machine_info.firstresult = True
pytest_benchmark_group_stats.firstresult = True
