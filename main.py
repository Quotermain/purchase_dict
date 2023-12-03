

def purchase_file_to_dict(file_to_process):
    purchases = dict()
    with open(file_to_process) as f:
        next(f)
        for line in f:
            key, value = line.split(', ')
            key = key.split(': ')[1].replace('"', '')
            value = value.split(': ')[1][:-2].replace('"', '')
            purchases[key] = value
    return purchases

if __name__ == "__main__":
    print(purchase_file_to_dict("purchase_log.txt"))
