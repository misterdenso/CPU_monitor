# import process

class Configure_widgets:

    def configure_cpu_bar(self):
        r = self.cpu.cpu_percent_return()
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'core {i + 1} usage: {r[i]}%')
            self.list_pbar[i].configure(value=r[i])

        y = self.cpu.mem_percent_return()
        self.ram_lab.configure(text=f'memory usage: {y[2]}%, used: {round(y[3] / 1024 / 1024 / 1024, 1)} Gb,\n'
                                    f' available: {round(y[4] / 1024 / 1024 / 1024, 1)} Gb')
        self.ram_bar.configure(value=y[2])

        self.wheel = self.after(1000, self.configure_cpu_bar)

    def configure_win(self):
        if self.wm_overrideredirect():
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()

    def clear_win(self):
        for i in self.winfo_children():
            i.destroy()

    # def configure_min(self):

