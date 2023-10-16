__author__ = "Alexios Nersessian"
__email__ = "nersessian@gmail.com"
__version__ = "1.0"


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
    keys = []

    try:
        # Open the CSV file
        with open(file_name, 'r') as f:
            raw = f.readlines()

        for i, line in enumerate(raw):
            tmp = line.replace("\n", "").split(",")

            if i > 0:
                for x, key in enumerate(keys):
                    tmp_dict[key] = tmp[x+1]
                information_dict[tmp[column_as_key-1]] = tmp_dict

            else:
                for field in tmp:
                    keys.append(field)
                keys.pop(0)
            tmp_dict = {}

        return information_dict

    except Exception as e:
        print(e)
        return {"Error": e}
