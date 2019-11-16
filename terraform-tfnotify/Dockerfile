FROM hashicorp/terraform:light
RUN wget https://github.com/mercari/tfnotify/releases/download/v0.3.0/tfnotify_v0.3.0_linux_amd64.tar.gz && \
tar xvzf tfnotify_v0.3.0_linux_amd64.tar.gz && \
mv tfnotify_*_linux_amd64/tfnotify /usr/local/bin/tfnotify && \
rm -r tfnotify_*_linux_amd64*
RUN wget https://github.com/hyperonecom/terraform-provider-hyperone/releases/download/0.0.1/terraform-provider-rootbox_0.0.1_linux_amd64.tar.gz && \
tar xvzf terraform-provider-rootbox_0.0.1_linux_amd64.tar.gz && \
mv terraform-provider-rootbox_0.0.1 /usr/local/bin/terraform-provider-rootbox
