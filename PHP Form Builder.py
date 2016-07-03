import sublime, sublime_plugin

class CompletionTriggerCommand(sublime_plugin.TextCommand):
    def run(self, edit, completionTriggerText):
        self.view.insert(edit, self.view.sel()[0].begin(), completionTriggerText)
        self.view.run_command("auto_complete")
        self.view.run_command("insert_best_completion")

class phpFormBuilderCommand(sublime_plugin.TextCommand):
    def on_quick_panel_selection(self, index):
        if index == -1:
            return
        else:
            self.view.run_command('completion_trigger', {"completionTriggerText": self.completions_trigger[index]})
    def run(self, edit):
        self.form_element_labels = [
            'new Form($form_ID, $layout = \'horizontal\', $attr = \'\');',
            'setAction($url, $add_get_vars = true)',
            'setOptions();',
            'setMethod($method);',
            'startFieldset($legend = \'\')',
            'endFieldset()',
            'startDependantFields($parent_field, $show_values)',
            'endDependantFields()',
            'setCols($labelsCols, $fieldsCols, $breakpoint = \'sm\')',
            'addIcon($input_name, $icon_html, $pos)',
            'addInput--function--($type, $name, $value = \'\', $label = \'\', $attr = \'\')',
            'addInputWrapper($html, $element_name)',
            'groupInputs($input1, $input2, $input3 = \'\')',
            'addTextarea($name, $value = \'\', $label = \'\', $attr = \'\')',
            'addOption($select_name, $value, $txt, $group_name = \'\', $attr = \'\')',
            'addSelect($select_name, $label = \'\', $attr = \'\', $displayGroupLabels = true)',
            'addCountrySelect($select_name, $label = \'\', $attr = \'\', $user_options = array())',
            'addRadio($group_name, $label, $value, $attr)',
            'printRadioGroup($group_name, $label = \'\', $inline = true, $attr = \'\')',
            'addCheckbox($group_name, $label, $name, $value, $attr)',
            'printCheckboxGroup($group_name, $label = \'\', $inline = true, $attr = \'\')',
            'addBtn($type, $name, $value, $text, $attr = \'\', $btnGroupName = \'\')',
            'printBtnGroup($btnGroupName, $label = \'\')',
            'addHtml($html, $element_name = \'\', $pos = \'after\')',
            'addPlugin($plugin_name, $selector, $js_content = \'default\', $js_replacements = \'\')',
            'addFileUpload($type, $name, $value = \'\', $label = \'\', $attr = \'\', $fileUpload_config = \'\')',
            'printIncludes($type)',
            'render($debug = false)',
            'printJsCode()',
            'Form::sendMail($from_email, $adress, $subject, $filter_values = \'\', $values = \'\')',
            'Form::sendAdvancedMail($options, $values = \'\')',
            'Form::registerValues($form_ID)',
            'Form::mergeValues(array(\'step-form-1\', \'step-form-2\', \'step-form-3\'))',
            'Form::clear($form_ID)'
        ]
        self.completions_trigger = [
            'newForm',
            'setAction',
            'setOptions',
            'startFieldset',
            'endFieldset',
            'startDependantFields',
            'endDependantFields',
            'addInput--function--',
            'addInputWrapper',
            'groupInputs',
            'addTextarea',
            'addOption',
            'addSelect',
            'addCountrySelect',
            'addRadio',
            'printRadioGroup',
            'addCheckbox',
            'printCheckboxGroup',
            'addBtn',
            'printBtnGroup',
            'addHtml',
            'addPlugin',
            'addFileUpload',
            'printIncludes',
            'render',
            'printJsCode',
            'FormSendMail',
            'FormSendAdvancedMail',
            'FormRegisterValues',
            'FormMergeValues',
            'FormClear'
        ]
        self.view.window().show_quick_panel(self.form_element_labels, self.on_quick_panel_selection)
