# Creates a device with *two* qubits
dev = qp.device("default.qubit", wires=2)


@qp.qnode(dev)
def two_qubit_circuit():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE |+>|1>
    qp.Hadamard(wires=0)
    qp.PauliX(wires=1)
    # RETURN TWO EXPECTATION VALUES, Y ON FIRST QUBIT, Z ON SECOND QUBIT

    return [qml.expval(qml.PauliY(wires = 0)), qml.expval(qml.PauliZ(wires = 1))]
