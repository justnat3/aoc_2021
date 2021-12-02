def read_sample() -> str:
    try:
        with open('./sample4', 'r') as fd:
            sample = fd.read()
            return sample
    except Exception as f:
        raise f