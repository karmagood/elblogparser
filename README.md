## Installation
```
 virtualenv elblogparser
 cd elblogparser
 git clone https://github.com/karmagood/elblogparser.git
 pip install -r requirements.txt
```
Now you can run parse.py with any options needed. Default columns ['count', 'client'] are printed into console.


## Usage: parse.py [OPTIONS]

```
Options:
  -l, --log_file TEXT     Log file to parse.
  -f, --folder TEXT       Log files folder path.
  -o, --output_file TEXT  Write result into a file. Path and name for a report
                          file.
  -c, --col TEXT          Columns to add to report.
  --limit INTEGER         Limit numbers of request to show or write to report.
  --client TEXT           Count only exact client.
  --backend TEXT          Count only exact backend.
  --request_type TEXT     Count only exact request types.
  --url TEXT              Count only exact url.
  --ascending             Sort in ascending order.
  --order_by INTEGER      Column number to order rows by. Starts from 0.
  --help                  Show this message and exit.
```
## Examples

Call with options

```
    python parse.py -f ~/logs_folder/ --col count --col requested_url --col client
    --col backend --col total_time --limit 10 --url example.com:443/api/cats
    --order_by 4

```

Output

```
```