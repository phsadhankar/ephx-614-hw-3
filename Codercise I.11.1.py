num_wires = 3
dev = qp.device("default.qubit", wires=num_wires)


@qp.qnode(dev)
def make_basis_state(basis_id):
    """Produce the 3-qubit basis state corresponding to |basis_id>.

    Note that the system starts in |000>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.

    Returns:
        np.array[complex]: The computational basis state |basis_id>.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    bin_id = np.binary_repr(basis_id, width = num_wires) # Control the number of binary bitsting
    for i, bit in enumerate(bin_id):
        if bit == '1': qp.PauliX(wires=i)
    # CREATE THE BASIS STATE

    return qp.state()


basis_id = 3
print(f"Output state = {make_basis_state(basis_id)}")
