import filesystemBuilder
import workingDirectory

def main():
    cwd = workingDirectory.FileSystemDir()
    print(cwd.homeDirectory)

    builder = filesystemBuilder.filesystemBuilder(cwd)

    builder.buildFileSystem()

if __name__ == '__main__':
    main()
