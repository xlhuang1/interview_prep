# Your task is to implement a simplified version of a file hosting service. All operations that should be supported
# are listed below. Partial credit will be granted for each test passed, so press “Submit” often to run tests and re -
# ceive partial credits for passed tests. Please check tests for requirements and argument types.

# Example of fire structure with various files:
# 1 ----- [server34] ----- 24000 Bytes Limit -------
# 2 ----------------------- Size -------
# 3 +- file-1.zip 4321 Bytes
# 4 +- dir-a
# 5 | +- dir-c
# 4
# 6 | | +- file-2.txt 1100 Bytes
# 7 | | +- file-3.csv 2122 Bytes
# 8 +- dir-b
# 9 | +- file-4.mdx 3378 Bytes


# Level 1 - Initial Design and Basic Functions
class File:

    def __init__(self, filename, size):
        self.filename = filename
        self.size = size
        self.timestamp = None
        self.ttl = None
        self.prev_timestamp = None
        self.prev_size = None

    def __init__(self, filename, size, timestamp):
        self.filename = filename
        self.size = size
        self.timestamp = timestamp
        self.ttl = None

    def __init__(self, filename, size, timestamp, ttl):
        self.filename = filename
        self.size = size
        self.timestamp = timestamp
        self.ttl = ttl

    def store_state(self, timestamp):


class Server:

    def __init__(self, server):
        self.server = server

    def file_has_ttl(self, file_name):
        # if file has ttl return True



    def FILE_UPLOAD_helper(self, file_name, size, line):
        if self.FILE_GET(file_name) is not None:
            raise FileExistsError('file with '+file_name+' already exists on server')
        self.server.append(line + " " + file_name + " " + str(size) + " Bytes")

    def FILE_UPLOAD(self, file_name, size):
        if self.FILE_GET(file_name) is not None:
            raise FileExistsError('file with '+file_name+' already exists on server')
        self.server.append(file_name + " " + str(size) + " Bytes")


    def FILE_GET(self, file_name):
        for line in self.server:
            if file_name in line:
                return line[1] # size
        return None


    def FILE_COPY(self, source, dest):
        if not source:
            raise FileNotFoundError('source file does not exist')
        self.server[dest] = source

# Level 2 - Data Structures and Data Processing
# Find top 10 files starting with the provided prefix. Order results by their size in descending
# order, and in case of a tie by file name.

    def FILE_SEARCH(self, prefix):
        # results filename : file size
        results = []

        for file in self.server:
            if prefix in file.file_name:
                # make sure prefix matches start of file only
                results.append((file.file_name, file.file_size))
                # note - in order to get top 10 files sorted by size, we need to get all files on server that match prefix
        # sorts by size descending first and then if there is tie orders by file name ascending
        sorted_results = sorted(results, key=lambda x: (x[1], -ord(x[0])), reverse=True)
        return sorted_results[:10]

# Level 3 - Refactoring and Encapsulation
# Files now might have a specified time to live on the server. Implement extensions of existing methods which inherit all functionality but also with an additional parameter to include a timestamp for the operation, and new
# files might specify the time to live - no ttl means lifetime being infinite.
    def FILE_UPLOAD_AT(self, timestamp, file_name, file_size):
        self.FILE_UPLOAD_helper(timestamp, file_name, file_name)

    def FILE_UPLOAD_AT(self, timestamp, file_name, file_size, ttl):
        line = timestamp + " " + ttl
        self.FILE_UPLOAD_helper(line, file_name, file_size)

    def FILE_GET_AT(self, timestamp, file_name):
        pass

    def FILE_COPY_AT(self, timestamp, file_from, file_to):
        pass

    def FILE_SEARCH_AT(self, timestamp, prefix):
        pass


