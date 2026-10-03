dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def prepare_state():
    ##################
    # YOUR CODE HERE #
    ##################
    qp.RY(np.pi/3, wires = 0)
    qp.RZ(-np.pi/2, wires = 0)
    # APPLY OPERATIONS TO PREPARE THE TARGET STATE

    return qp.state()
