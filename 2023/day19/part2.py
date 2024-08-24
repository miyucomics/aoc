workflows = {}

with open("input.txt") as file:
    workflows = {
        name: data[:-1].split(",")
        for raw in file.read().split("\n\n")[0].splitlines()
        for name, data in [raw.split("{")]
    }

def trace(workflow, quantum):
    if workflow == "R":
        return 0

    if workflow == "A":
        combinations = 1
        for span in quantum.values():
            combinations *= span[1] - span[0] + 1
        return combinations

    successes = 0

    for procedure in workflows[workflow][:-1]:
        threshold, next_workflow = procedure.split(":")
        threshold = int(threshold[2:])

        property = procedure[0]
        low, high = quantum[property]

        if procedure[1] == "<":
            passed = (low, threshold - 1)
            failed = (threshold, high)
        else:
            passed = (threshold + 1, high)
            failed = (low, threshold)

        if passed[0] <= passed[1]:
            copied = dict(quantum)
            copied[property] = passed
            successes += trace(next_workflow, copied)

        if failed[0] <= failed[1]:
            quantum = dict(quantum)
            quantum[property] = failed
        else:
            break
    else:
        successes += trace(workflows[workflow][-1], quantum)

    return successes

print(trace("in", {key: (1, 4000) for key in "xmas"}))
