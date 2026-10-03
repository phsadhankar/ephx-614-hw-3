dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def unitary_with_h_and_t():
    ##################
    # YOUR CODE HERE #
    ##################
    qp.Hadamard(wires=0)
    qp.T(wires=0)
    qp.Hadamard(wires=0)
    qp.T(wires=0)
    qp.T(wires=0)
    qp.Hadamard(wires=0)
    # APPLY ONLY H AND T TO PRODUCE A CIRCUIT THAT EFFECTS THE GIVEN MATRIX

    return qp.state()
