dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def prepare_state():
    ##################
    # YOUR CODE HERE #
    ##################
    qp.Hadamard(wires = 0)
    qp.RZ(np.pi * 1.25, wires = 0)
    # APPLY OPERATIONS TO PREPARE THE TARGET STATE

    return qp.state()
