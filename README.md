## Installation
```
 virtualenv elblogparser
 cd elblogparser
 git clone https://github.com/karmagood/elblogparser.git
 cd elblogparser
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
Possible columns 
    * timestamp \- * The time when the load balancer received the request from the client, in ISO 8601 format.*
    * elb \- * The name of the load balancer*
    * client \- * The IP address and port of the requesting client.*
    * backend \- * The IP address and port of the registered instance that processed this request.*
    * request_processing_time \- * The total time elapsed, in seconds, from the time the load balancer received the request until the time it sent it to a registered instance.*
    * backend_processing_time \- * The total time elapsed, in seconds, from the time the load balancer sent the request to a registered instance until the instance started to send the response headers.*
    * response_processing_time \- * The total time elapsed (in seconds) from the time the load balancer received the response header from the registered instance until it started to send the response to the client.*
    * elb_status_code \- * The status code of the response from the load balancer.*
    * backend_status_code \- * The status code of the response from the registered instance.*
    * received_bytes \- * The size of the request, in bytes, received from the client (requester).*
    * sent_bytes \- * The size of the response, in bytes, sent to the client (requester).*
    * request \- * The request line from the client enclosed in double quotes and logged in the following format: HTTP Method + Protocol://Host header:port + Path + HTTP version.*
    * user_agent \- * A User\- *Agent string that identifies the client that originated the request. The string consists of one or more product identifiers, product[/version]. If the string is longer than 8 KB, it is truncated.*
    * ssl_cipher \- * [HTTPS/SSL listener] The SSL cipher. This value is recorded only if the incoming SSL/TLS connection was established after a successful negotiation. Otherwise, the value is set to \- *.*
    * ssl_protocol \- * [HTTPS/SSL listener] The SSL protocol. This value is recorded only if the incoming SSL/TLS connection was established after a successful negotiation. Otherwise, the value is set to \- *.*
    * total_time \- * sum of request_processing_time, backend_processing_time, response_processing_time*
    * client_ip \- * client without port*
    * backend_ip \- * backend without port*
    * request_type \- * Request Type parsed from request*

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