from os import system
qg = """ quiet_git() {
    stdout=$(tempfile)
    stderr=$(tempfile)

    if ! git "$@" </dev/null >$stdout 2>$stderr; then
        cat $stderr >&2
        rm -f $stdout $stderr
        exit 1
    fi

    rm -f $stdout $stderr
}"""
def run_git(command):
    system(qg)
    system('quiet_git ' + command)
