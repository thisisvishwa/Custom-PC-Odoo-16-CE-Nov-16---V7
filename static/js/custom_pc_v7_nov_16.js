odoo.define('custom_pc_v7_nov_16', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');
    var rpc = require('web.rpc');

    var QWeb = core.qweb;
    var _t = core._t;

    var CustomPCBuilder = Widget.extend({
        template: 'component_selection_template',
        events: {
            'click .component-selection': 'onComponentSelection',
            'click .preview-build': 'onPreviewBuild',
            'click .save-build': 'onSaveBuild',
        },

        init: function (parent, options) {
            this._super(parent, options);
            this.components = [];
            this.build = {};
        },

        start: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                self.loadComponents();
            });
        },

        loadComponents: function () {
            var self = this;
            rpc.query({
                model: 'pc_components',
                method: 'search_read',
                args: [[]],
            }).then(function (components) {
                self.components = components;
                self.render();
            });
        },

        render: function () {
            this.$el.html(QWeb.render('component_selection_template', {components: this.components}));
        },

        onComponentSelection: function (event) {
            var componentId = $(event.currentTarget).data('id');
            var component = _.findWhere(this.components, {id: componentId});
            this.build[component.type] = component;
        },

        onPreviewBuild: function () {
            this.$el.html(QWeb.render('pc_build_preview_template', {build: this.build}));
        },

        onSaveBuild: function () {
            rpc.query({
                model: 'saved_pc_builds',
                method: 'create',
                args: [this.build],
            }).then(function () {
                alert(_t('Build saved successfully!'));
            });
        },
    });

    core.action_registry.add('custom_pc_v7_nov_16', CustomPCBuilder);

    return CustomPCBuilder;
});