from collections import deque
import os


class Catalog(object):
	def recFindFile(self, root, depth):
		if os.path.isdir(root):
			depth += 1
			for i in os.listdir(root):
				print('{}{}{}'.format(depth, depth * 4 * " ", os.path.basename(root)))
				full_path = os.path.join(root, i)
				self.recFindFile(full_path, depth)
		else:
			print('{}{}{}'.format(depth, depth * 4 * " ", os.path.basename(root)))


if __name__ == "__main__":
	cat = Catalog()
	cat.recFindFile('G:\编程资料\老男孩Python全栈开发 前端+web', 0)
