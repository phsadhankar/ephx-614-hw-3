# An array to store your results
shot_results = []

# Different numbers of shots
shot_values = [100, 1000, 10000, 100000, 1000000]

for shots in shot_values:
    ##################
    # YOUR CODE HERE #
    ##################
    dev = qp.device('default.qubit', wires=1, shots=shots)
    # CREATE A DEVICE, CREATE A QNODE, AND RUN IT
    @qp.qnode(dev)
    def circuit():
        qp.RX(np.pi/4, wires=0)
        qp.Hadamard(wires=0)
        qp.PauliZ(wires=0)
        return qp.expval(qp.PauliY(wires=0))

    output = circuit()
    # STORE RESULT IN SHOT_RESULTS ARRAY
    shot_results.append(output)

print(qp.math.unwrap(shot_results))
