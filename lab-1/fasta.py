"""
Parse every FASTA record from stdin and print each.
"""

class FASTAReader( object ):
    def __init__( self, file ):
        self.file = file
        self.last_id = None
        
    def __iter__( self ):
        return self
        
    def next( self ):
        if self.last_id is None:
            line = self.file.readline()
            if line == "":
                raise StopIteration
            # Verify is header line
            assert line.startswith( ">" )
            # Extract id -- whole line
            ## identifier = line[1:].rstrip( "\r\n" )
            # Extract id -- space
            identifier = line[1:].split()[0]
        else:
            identifier = self.last_id

        sequences = []

        while True:
            line = self.file.readline().rstrip("\r\n")
            if line.startswith( ">" ):
                self.last_id = line[1:].split()[0]
                break
            elif line == "":
                if sequences:
                    return identifier, "".join( sequences )
                ## return None, None
                raise StopIteration
            else:
                sequences.append( line )
                
        return identifier, "".join( sequences )

#
# """
# Parse every FASTA record from stdin and print each
# """
#
# import sys
#
# class FASTAReader(object):
#     def __init__(self, file):
#         self.file = file
#         self.last_id = None
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.last_id is None:
#             line = self.file.readline()
#             # verify header line starts with >
#             assert line.startswith(">")
#             # extract id - whole line
#             ## identifier = line[1:].rstrip("\n\r")
#             # extract id - space (after the carrot sign, before the space)
#             identifier = line[1:].split()[0]
#         else:
#             identifier = self.last_id
#
#         # list to store sequence
#         sequences = []
#
#         # loop forever (no condidtion)
#         while 1:
#             line = self.file.readline().rstrip("\r\n")
#             if line.startswith(">"):
#                 self.last_id = line[1:].split()[0]
#                 break
#             elif line == "":
#                 ## return None, None
#                 if sequences:
#                     return identifier, "".join(sequences)
#                 raise StopIteration
#             else:
#                 sequences.append(line)
#
#         return identifier, "".join(sequences)
#
