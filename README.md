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
    * timestamp \- _ The time when the load balancer received the request from the client, in ISO 8601 format._
    * elb \- _ The name of the load balancer_
    * client \- _ The IP address and port of the requesting client._
    * backend \- _ The IP address and port of the registered instance that processed this request._
    * request_processing_time \- _ The total time elapsed, in seconds, from the time the load balancer received the request until the time it sent it to a registered instance._
    * backend_processing_time \- _ The total time elapsed, in seconds, from the time the load balancer sent the request to a registered instance until the instance started to send the response headers._
    * response_processing_time \- _ The total time elapsed (in seconds) from the time the load balancer received the response header from the registered instance until it started to send the response to the client._
    * elb_status_code \- _ The status code of the response from the load balancer._
    * backend_status_code \- _ The status code of the response from the registered instance._
    * received_bytes \- _ The size of the request, in bytes, received from the client (requester)._
    * sent_bytes \- _ The size of the response, in bytes, sent to the client (requester)._
    * request \- _ The request line from the client enclosed in double quotes and logged in the following format: HTTP Method + Protocol://Host header:port + Path + HTTP version._
    * user_agent \- _ A User\- _Agent string that identifies the client that originated the request. The string consists of one or more product identifiers, product[/version]. If the string is longer than 8 KB, it is truncated._
    * ssl_cipher \- _ [HTTPS/SSL listener] The SSL cipher. This value is recorded only if the incoming SSL/TLS connection was established after a successful negotiation. Otherwise, the value is set to \- _._
    * ssl_protocol \- _ [HTTPS/SSL listener] The SSL protocol. This value is recorded only if the incoming SSL/TLS connection was established after a successful negotiation. Otherwise, the value is set to \- _._
    * total_time \- _ sum of request_processing_time, backend_processing_time, response_processing_time_
    * client_ip \- _ client without port_
    * backend_ip \- _ backend without port_
    * request_type \- _ Request Type parsed from request_

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