dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def apply_h_and_measure(state):
    """Complete the function such that we apply the Hadamard gate
    and measure in the computational basis.

    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise leave it in state 0.

    Returns:
        np.array[float]: The measurement outcome probabilities.
    """
    if state == 1:
        qp.PauliX(wires=0)

    ##################
    # YOUR CODE HERE #
    ##################
    qp.Hadamard(wires=0)
    # APPLY HADAMARD AND MEASURE

    return qp.probs(wires=0)


print(apply_h_and_measure(0))
print(apply_h_and_measure(1))
