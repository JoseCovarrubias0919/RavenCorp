class EstacionTrabajo {
    private int cantidadUnidades;
    private int tipoUnidades;

    public EstacionTrabajo(int cantidadUnidades, int tipoUnidades) {
        this.cantidadUnidades = cantidadUnidades;
        this.tipoUnidades = tipoUnidades;
    }

    public int calcularCostoProduccion() {
        int costoProduccion = (tipoUnidades == 1) ? 27 : 34;
        return costoProduccion * cantidadUnidades;
    }

    public int getTipoUnidades() {
        return tipoUnidades;
    }
}

