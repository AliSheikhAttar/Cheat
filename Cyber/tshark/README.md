# tshark


[wireshark cli](https://www.wireshark.org/docs/man-pages/tshark.html)

tshark [ -i <capture interface>|- ] [ -f <capture filter> ] [ -2 ] [ -r <infile> ] [ -w <outfile>|- ] [ options ] [ <filter> ]

tshark -G [ <report type> ] [ --elastic-mapping-filter <protocols> ]

## options
### -a|--autostop <capture autostop condition>
Specify a criterion that specifies when TShark is to stop writing to a capture file. The criterion is of the form test:value, where test is one of:

- duration:value Stop writing to a capture file after value seconds have elapsed. Floating point values (e.g. 0.5) are allowed.

- files:value Stop writing to capture files after value number of files were written.

- filesize:value Stop writing to a capture file after it reaches a size of value kB. If this option is used together with the -b option, TShark will stop writing to the current capture file and switch to the next one if filesize is reached. When reading a capture file, TShark will stop reading the file after the number of bytes read exceeds this number (the complete packet will be read, so more bytes than this number may be read). Note that the filesize is limited to a maximum value of 2 GiB.

- packets:value switch to the next file after it contains value packets. This does not include any packets that do not pass the display filter, so it may differ from -c<capture packet count>.

### -b|--ring-buffer <capture ring buffer option>
Cause TShark to run in "multiple files" mode. In "multiple files" mode, TShark will write to several capture files. When the first capture file fills up, TShark will switch writing to the next file and so on.

The created filenames are based on the filename given with the -w option, the number of the file and on the creation date and time, e.g. outfile_00001_20240714120117.pcap, outfile_00002_20240714120523.pcap, …​

With the files option it’s also possible to form a "ring buffer". This will fill up new files until the number of files specified, at which point TShark will discard the data in the first file and start writing to that file and so on. If the files option is not set, new files filled up until one of the capture stop conditions match (or until the disk is full).

The criterion is of the form key:value, where key is one of:

- duration:value switch to the next file after value seconds have elapsed, even if the current file is not completely filled up. Floating point values (e.g. 0.5) are allowed.

- files:value begin again with the first file after value number of files were written (form a ring buffer). This value must be less than 100000. Caution should be used when using large numbers of files: some filesystems do not handle many files in a single directory well. The files criterion requires either duration, interval or filesize to be specified to control when to go to the next file. It should be noted that each -b parameter takes exactly one criterion; to specify two criterion, each must be preceded by the -b option.

- filesize:value switch to the next file after it reaches a size of value kB. Note that the filesize is limited to a maximum value of 2 GiB.

- interval:value switch to the next file when the time is an exact multiple of value seconds. For example, use 3600 to switch to a new file every hour on the hour.

- packets:value switch to the next file after it contains value packets.

- nametimenum:value Choose between two save filename templates. If value is 1, make running file number part before start time part; this is the original and default behaviour (e.g. log_00001_20240714164426.pcap). If value is greater than 1, make start time part before running number part (e.g. log_20210828164426_00001.pcap). The latter makes alphabetical sorting order equal to creation time order, and keeps related multiple file sets in same directory close to each other.

Example: tshark -b filesize:1000 -b files:5 results in a ring buffer of five files of size one megabyte each.

### -i|--interface <capture interface> | -
Set the name of the network interface or pipe to use for live packet capture.

Network interface names should match one of the names listed in "tshark -D" (described above); a number, as reported by "tshark -D", can also be used.

If no interface is specified, TShark searches the list of interfaces, choosing the first non-loopback interface if there are any non-loopback interfaces, and choosing the first loopback interface if there are no non-loopback interfaces. If there are no interfaces at all, TShark reports an error and doesn’t start the capture.

Pipe names should be either the name of a FIFO (named pipe) or "-" to read data from the standard input. On Windows systems, pipe names must be of the form "\\.\pipe\pipename". Data read from pipes must be in standard pcapng or pcap format. Pcapng data must have the same endianness as the capturing host.

"TCP@<host>:<port>" causes TShark to attempt to connect to the specified port on the specified host and read pcapng or pcap data.

This option can occur multiple times. When capturing from multiple interfaces, the capture file will be saved in pcapng format.

### -P|--print
Decode and display the packet summary or details, even if writing raw packet data using the -w option, and even if packet output is otherwise suppressed with -Q.

### -q
When capturing packets, don’t display the continuous count of packets captured that is normally shown when saving a capture to a file; instead, just display, at the end of the capture, a count of packets captured. On systems that support the SIGINFO signal, such as various BSDs, you can cause the current count to be displayed by typing your "status" character (typically control-T, although it might be set to "disabled" by default on at least some BSDs, so you’d have to explicitly set it to use it).

### -Q
When capturing packets, don’t display, on the standard error, the initial message indicating on which interfaces the capture is being done, the continuous count of packets captured shown when saving a capture to a file, and the final message giving the count of packets captured. Only true errors are displayed on the standard error.

This outputs less than the -q option, so the interface name and total packet count and the end of a capture are not sent to stderr.

When reading a capture file, or when capturing and not saving to a file, don’t print packet information; this is useful if you’re using a -z option to calculate statistics and don’t want the packet information printed, just the statistics.