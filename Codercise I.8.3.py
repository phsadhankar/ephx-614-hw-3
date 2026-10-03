v = np.array([0.52889389 - 0.14956775j, 0.67262317 + 0.49545818j])

##################
# YOUR CODE HERE #
##################

# CREATE A DEVICE
dev = qp.device('default.qubit', wires=1)
@qp.qnode(dev)
# CONSTRUCT A QNODE THAT USES qp.MottonenStatePreparation
# TO PREPARE A QUBIT IN STATE V, AND RETURN THE STATE


def prepare_state(state=v):
    qp.StatePrep(state, wires = 0)
    return qp.state()


# This will draw the quantum circuit and allow you to inspect the output gates
print(prepare_state(v))
print()
print(qp.draw(prepare_state, level="device")(v))
