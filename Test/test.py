FCFlags = {"SYFCFlag": '', 'SYFCFlag':'', 'SMFCFlag': '',
           'SDFCFlag': '', 'EYFCFlag': '', 'EMFCFlag': ''}
FCFlags["SYFCFlag"] = False
if False in FCFlags.values():
    print(1)
print(FCFlags)
