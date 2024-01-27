def driver_ids(param):
    """ 
    create webdriver fixture parametrization id from `param`

    :param [(str, object)] param: represents a parameter passed to a
    webdriver initialization fixture. The first item in the tuple is
    expected to be the parameter id, while the second is expected to
    be a remote webdriver options object.
    """
    return param[0]

def init_driver(use_remote, remote_driver, local_driver, options):
    """
    create and initialize a webdriver instance.

    :param bool use_remote: If this is True, use a remote driver
    otherwise use a local webdriver.

    :param [function] local_driver: a local webdriver factory function

    :param [function] remote_driver: a local webdriver factory function.
    Accepts a remote webdriver options object as argument.

    :param [object] options: a remote webdriver options object.
    """

    if use_remote:
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        driver = remote_driver(options)
    else:
        driver = local_driver()

    driver.maximize_window()

    return driver
