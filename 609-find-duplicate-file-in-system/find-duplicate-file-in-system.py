class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dir=defaultdict(list)
        for path in paths:
            directory,*files=path.split()
            for file in files:
                filename, content=file.split('(')
                dir[content].append(directory+'/'+filename)

        return [paths for paths in dir.values() if len(paths)>1]