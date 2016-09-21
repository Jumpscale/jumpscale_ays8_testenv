from JumpScale import j


class Actions():

    def input(self, job):
        """
        create key, if it doesn't exist
        """

        # THIS ONE IS FIXED

        args = {}

        if 'key.path' in job.model.args:
            path = job.model.args['key.path']
            if not j.sal.fs.exists(path, followlinks=True):
                raise j.exceptions.Input(message="Cannot find ssh key:%s for service:%s" %
                                         (path, job.service), level=1, source="", tags="", msgpub="")

            args["key.priv"] = j.sal.fs.fileGetContents(path)
            args.pop('key.path')

        if 'key.name' in job.model.args:
            path = j.do.getSSHKeyPathFromAgent("kds")
            if not j.sal.fs.exists(path, followlinks=True):
                raise j.exceptions.Input(message="Cannot find ssh key:%s for service:%s" %
                                         (path, job.service), level=1, source="", tags="", msgpub="")

            args["key.priv"] = j.sal.fs.fileGetContents(path)
            args.pop('key.priv')

        if 'key.priv' not in args or args['key.priv'].strip() == "":
            print("lets generate private key")
            path = j.sal.fs.joinPaths(j.dirs.tmpDir, "privatekey")
            j.sal.fs.remove(path)
            cmd = "ssh-keygen -q -t rsa -f %s -N ''" % (path)
            rc, out = j.sal.process.execute(cmd, die=True, outputToStdout=False, ignoreErrorOutput=False)
            args["key.priv"] = j.sal.fs.fileGetContents(path)

        return args
