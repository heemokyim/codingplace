def sanitize(arg_list):
    for idx in range(len(arg_list)):
        if ':' in arg_list[idx]:
            arg_list[idx]=arg_list[idx].replace(':','.')

        elif '-' in arg_list[idx]:
            arg_list[idx]=arg_list[idx].replace('-','.')

    return arg_list
