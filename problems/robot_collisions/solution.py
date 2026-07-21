class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        robots.sort()
        stack = []
        alive = []
        for robot in robots:
            pos, health, direction, index = robot
            if direction == 'R':
                stack.append(robot)
            else:
                while stack and health > 0:
                    right = stack[-1]
                    if right[1] < health:
                        stack.pop()
                        health -= 1
                    elif right[1] == health:
                        stack.pop()
                        health = 0
                    else:
                        right[1] -= 1
                        health = 0
                if health > 0:
                    robot[1] = health
                    alive.append(robot)
        alive.extend(stack)
        alive.sort(key=lambda x: x[3])
        ans = []
        for robot in alive:
            ans.append(robot[1])
        return ans