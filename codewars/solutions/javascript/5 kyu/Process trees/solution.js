let makeProcessTree = (processes) => {
    let processesMap = new Map(processes.map(info => [info.pid, new Process(info.pid, [])]));
    let root = null;

    for (let info of processes) {
        if (info.ppid === -1)
            root = processesMap.get(info.pid);
        else
            processesMap.get(info.ppid).children.push(processesMap.get(info.pid));
    }

    return root;
};