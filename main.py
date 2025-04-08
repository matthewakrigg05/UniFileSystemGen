import courseContext
import filesystemBuilder
import workingDirectory


def main():
    cwd = workingDirectory.FileSystemDir()
    course = courseContext.courseContext()

    builder = filesystemBuilder.fileSystemBuilder(cwd, course)

    builder.buildFileSystem()


if __name__ == '__main__':
    main()
