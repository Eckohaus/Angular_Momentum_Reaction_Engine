class AmreHeader extends HTMLElement {
    connectedCallback() {
        const moduleTitle = this.getAttribute('module-title') || 'AMRE SYSTEM NODE';
        const linkPath = this.getAttribute('link-path') || '172.232.237.109:8080';

        this.innerHTML = `
            <style>
                .amre-global-header { border-bottom: 1px dashed #005500; padding-bottom: 10px; margin-bottom: 25px; }
                .amre-global-header h2 { color: #00ff00; font-size: 16px; text-transform: uppercase; letter-spacing: 2px; margin: 0 0 5px 0; }
                .amre-global-header .sys-text { color: #008800; font-size: 10px; text-transform: uppercase; display: block; }
            </style>
            <div class="amre-global-header">
                <h2>${moduleTitle}</h2>
                <span class="sys-text">Engine: Fortran CGI Double-Precision Array | Link: ${linkPath}</span>
            </div>
        `;
    }
}
customElements.define('amre-header', AmreHeader);
