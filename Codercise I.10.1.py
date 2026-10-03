dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def circuit():
    ##################
    # YOUR CODE HERE #
    ##################
    qp.RX(np.pi/4, wires=0)
    qp.Hadamard(wires=0)
    qp.PauliZ(wires=0)
    # IMPLEMENT THE CIRCUIT IN THE PICTURE AND MEASURE PAULI Y

    return qp.expval(qml.PauliY(wires=0))

print(circuit())
