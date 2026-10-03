dev = qp.device("default.qubit", wires=2)


@qp.qnode(dev)
def create_one_minus():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE |1>|->
    qp.PauliX(wires=0)
    qp.Hadamard(wires=1)
    qp.PauliZ(wires=1)
    # RETURN A SINGLE EXPECTATION VALUE Z \otimes X

    return qp.expval(qp.PauliZ(0) @ qp.PauliX(1))


print(create_one_minus())
