__author__ = "Alexios Nersessian"
__email__ = "nersessian@gmail.com"
__version__ = "1.1"


def csv_to_dict(file_name:str, column_as_key:int) -> dict:
    """
    Pass the filename and column number of the CSV file that you would like to make the keys in the
    dictionary. For example Column One is 1 and Column five is 5.
              usage: csv_to_dict("example.csv", 2)
    :param file_name: string
    :param column_as_key: integer
    :return: dictionary
    """
    information_dict = {}
    tmp_dict = {}

    try:
        # Open the CSV file
        with open(file_name, 'r') as f:
            raw = f.readlines()

        keys = raw[:1][0].strip().split(',')
        keys.pop(column_as_key-1)

        for i, line in enumerate(raw[1:]):
            tmp = line.replace("\n", "").split(",")
            master_key = tmp[column_as_key-1]
            tmp.pop(column_as_key-1)

            for x, key in enumerate(keys):
                tmp_dict[key] = tmp[x]

            information_dict[master_key] = tmp_dict

            tmp_dict = {}

        return information_dict

    except Exception as e:
        print(e)
        return {"Error": e}
