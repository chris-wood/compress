import sys

MAX_DICT_SIZE = 4096

def main(argv):
    indata = ""
    for line in sys.stdin:
        indata = indata + line
    indata = indata.strip()

    ldict = {}
    for i in range(256):
        ldict[chr(i)] = i

    # SETUP
    print "Initial input:  %s" % (indata)

    # COMPRESS
    outdata = []
    s = ""
    for c in indata:
        ss = s + c
        if ss in ldict:
            s = ss
        else:
            print "Encoding %s %d" % (s, (ldict[s]))
            outdata.append(ldict[s])
            ldict[ss] = len(ldict)
            s = c

    print "Encoded output: %s" % (outdata)

    # DECOMPRESS
    rdict = {}
    for i in range(256):
        rdict[i] = chr(i)

    fdata = []
    prevcode = outdata[0]
    fdata.append(rdict[prevcode])
    for c in outdata[1:]:
        currcode = c
        entry = rdict[currcode]
        fdata.append(entry)
        ch = entry[0]
        
        prev_entry = rdict[prevcode] + ch
        rdict[len(rdict)] = prev_entry

        prevcode = currcode
    
    print "Decoded output: %s" % ("".join(fdata))

if __name__ == "__main__":
    main(sys.argv[1:])
