FROM hashicorp/terraform:0.13.4
RUN wget https://github.com/mercari/tfnotify/releases/download/v0.3.0/tfnotify_v0.3.0_linux_amd64.tar.gz && \
tar xvzf tfnotify_v0.3.0_linux_amd64.tar.gz && \
mv tfnotify_*_linux_amd64/tfnotify /usr/local/bin/tfnotify && \
rm -r tfnotify_*_linux_amd64*
RUN wget https://github.com/hyperonecom/terraform-provider-hyperone/releases/download/0.0.1/terraform-provider-rootbox_0.0.1_linux_amd64.tar.gz && \
wget https://github.com/hyperonecom/terraform-provider-hyperone/releases/download/0.0.1/terraform-provider-hyperone_0.0.1_linux_amd64.tar.gz && \
tar xvzf terraform-provider-rootbox_0.0.1_linux_amd64.tar.gz && \
tar xvzf terraform-provider-hyperone_0.0.1_linux_amd64.tar.gz && \
PLUGIN_DIR="/bin" && \
mkdir -p "$PLUGIN_DIR" && \
mv terraform-provider-rootbox_0.0.1 "${PLUGIN_DIR}/terraform-provider-rootbox" && \
mv terraform-provider-hyperone_0.0.1 "${PLUGIN_DIR}/terraform-provider-hyperone" && \
rm terraform-provider-rootbox_0.0.1_linux_amd64.tar.gz && \
rm terraform-provider-hyperone_0.0.1_linux_amd64.tar.gz
