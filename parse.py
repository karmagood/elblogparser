import os
import click
import csv
from collections import OrderedDict


def count(file, col, client, backend, request_type, url):
    counted_requests = {}
    with open(file) as log_file:
        filereader = csv.reader(log_file, delimiter=" ")
        for line in filereader:
            request = {}
            request["timestamp"], \
            request["elb"], \
            request["client"], \
            request["backend"], \
            request["request_processing_time"], \
            request["backend_processing_time"], \
            request["response_processing_time"], \
            request["elb_status_code"], \
            request["backend_status_code"], \
            request["received_bytes"], \
            request["sent_bytes"], \
            request["request"], \
            request["user_agent"], \
            request["ssl_cipher"], \
            request["ssl_protocol"] = line
            request["total_time"] = float(request["request_processing_time"]) \
                                    + float(request["backend_processing_time"]) \
                                    + float(request["response_processing_time"])
            request["client_ip"] = request["client"][:-5]
            request["backend_ip"] = request["backend"][:-5]
            request["request_type"], request["requested_url"], request['protocol'] = request['request'].split(" ")
            if not client: client = ("",)
            if not backend: backend = ("",)
            if not request_type: request_type = ("",)
            if not url: url = ("",)
            if any(cl in request["client"] for cl in client) and \
                    any(bk in request["backend"] for bk in backend) and \
                    any(rt in request["request_type"] for rt in request_type) and \
                    any(ur in request["request"] for ur in url):
                request_key = tuple(request[val] for val in col if val != 'count')
                if not counted_requests.get(request_key):
                    counted_requests[request_key] = 1
                else:
                    counted_requests[request_key] += 1
    return counted_requests


def order(requests, col, ascending, order_by):
    list_requests = []
    for item in requests.items():
        item_list = [i for i in item[0]]
        item_list.insert(col.index('count'), item[1])
        list_requests.append(item_list)
    return list(sorted(list_requests, key=lambda t: t[order_by], reverse=not ascending))


def write_report(requests, limit, output_file):
    if output_file:
        with open(output_file, "w+") as report:
            for request in requests[:limit+1]:
                report.write(" ".join(list(map(str, request))+["\n"]))
    else:
        for request in requests[:limit+1]:
            print(" ".join(list(map(str, request))))


@click.command()
@click.option('--log_file', '-l', type=str, help="Log file to parse.", multiple=True)
@click.option('--folder', '-f', type=str, help="Log files folder path.")
@click.option('--output_file', '-o', type=str, help="Write result into a file. Path and name for a report file.")
@click.option('--col', '-c', default=['count', 'client'], help="Columns to add to report. ", multiple=True)
@click.option('--limit', default=None, type=int, help="Limit numbers of request to show or write to report.")
@click.option('--client', type=str, help="Count only exact client.", multiple=True)
@click.option('--backend', type=str, help="Count only exact backend.", multiple=True)
@click.option('--request_type', type=str, help="Count only exact request types.", multiple=True)
@click.option('--url', type=str, help="Count only exact url.", multiple=True)
@click.option('--ascending', is_flag=True, help="Sort in ascending order.")
@click.option('--order_by', default=0, type=int, help="Column number to order rows by. Starts from 0.")
def main(log_file, folder, output_file, col, limit, client, backend, request_type, url, ascending, order_by):
    counted_requests_all = {}
    path_to = ""
    files = log_file
    if folder:
        files = os.listdir(folder)
        path_to = folder
    with click.progressbar(files, label='Parsing Log files.') as files_bar:
        for logs in files_bar:
            counted_requests = count(os.path.join(path_to, logs), col, client, backend, request_type, url)
            for key in counted_requests.keys():
                if not counted_requests_all.get(key):
                    counted_requests_all[key] = counted_requests[key]
                else:
                    counted_requests_all[key] += counted_requests[key]
        counted_requests = order(counted_requests_all, col, ascending, order_by)
        write_report(counted_requests, limit, output_file)


if __name__ == '__main__':
    main()
