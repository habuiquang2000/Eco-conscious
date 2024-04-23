def host(req):
    return {
        'host_domain': req._current_scheme_host
    }
