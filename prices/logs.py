def write_log_txt(data):
    with open('logs.txt', 'w') as logs_file:
        logs_file.write(data)
    print('Logs file write successfully')


def read_log_txt(data):
    with open('logs.txt', 'r') as logs_file:
        logs_file.write(data)
    print('Logs file write successfully')
