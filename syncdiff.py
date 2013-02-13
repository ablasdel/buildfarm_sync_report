import difflib
import argparse


def main():
    usage = "usage: %prog fromfile tofile"
    parser = argparse.ArgumentParser(usage)
    parser.add_argument('fromfile', type=str, nargs='+', default=None)
    parser.add_argument('tofile', type=str, nargs='+', default=None)
    args = parser.parse_args()

    files = [args.fromfile[0], args.tofile[0]]
    fromlines = open(files[0], 'U').readlines()
    tolines = open(files[1], 'U').readlines()
    diff = difflib.unified_diff(fromlines, tolines, files[0], files[1], n=5)
    diff = [l for l in diff if ('Version:' in l or 'Package:' in l)]

    added_packages = {}
    removed_packages = {}
    versioned_packages = {}

    current_package = None
    current_package_mod = None
    current_version = None
    current_version_mod = None
    for line in diff:
        if 'Package:' in line:
            current_package = line[line.index(':') + 2:-1]
            current_package_mod = line[0]
        elif 'Version:' in line:
            current_version = line[line.index(':') + 2:-1]
            current_version_mod = line[0]
            if current_package_mod is ' ':
                if current_package in versioned_packages:
                    versioned_packages[current_package].append(current_version)
                    versioned_packages[current_package].sort()
                    if len(versioned_packages[current_package]) > 2:
                        raise Exception(current_package + ": more than 2 ver")
                else:
                    versioned_packages[current_package] = [current_version]
            elif current_package_mod is '+':
                if current_version_mod is not '+':
                    raise Exception(current_package + " add package odd ver")
                if current_package in removed_packages:
                    temp = [current_version, removed_packages[current_package]]
                    del removed_packages[current_package]
                    versioned_packages[current_package] = temp
                    versioned_packages[current_package].sort()
                else:
                    added_packages[current_package] = current_version
            elif current_package_mod is '-':
                if current_version_mod is not '-':
                    raise Exception(current_package + " rem package odd ver")
                if current_package in added_packages:
                    temp = [current_version, added_packages[current_package]]
                    del added_packages[current_package]
                    versioned_packages[current_package] = temp
                    versioned_packages[current_package].sort()
                else:
                    removed_packages[current_package] = current_version
            else:
                raise Exception("Erronious character: " + current_package_mod)
        else:
            raise Exception("Erronious line found: " + line)

    print "\nPackages Added: "
    for line in sorted(added_packages):
        print line, ':', added_packages[line]
    print "\nPackages Removed: "
    for line in sorted(removed_packages):
        print line, ':', removed_packages[line]
    print "\nPackages Updated: "
    for line in sorted(versioned_packages):
        print_package = versioned_packages[line]
        if len(print_package) == 2:
            print line, ':', print_package[0], '->', print_package[1]

if __name__ == '__main__':
    main()
