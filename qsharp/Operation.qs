namespace Bell {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    operation MeasureEntanglement() : Result[] {
        use qubits = Qubit[2];
        H(qubits[0]);
        CNOT(qubits[0], qubits[1]);
        return MultiM(qubits);
    }
}