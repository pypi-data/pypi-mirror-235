!function(){"use strict";var e,t;e=Djblets.Config.ListItem.extend({defaults:_.defaults({extension:null},Djblets.Config.ListItem.prototype.defaults),initialize(){Djblets.Config.ListItem.prototype.initialize.apply(this,arguments),this._updateActions(),this._updateItemState(),this.listenTo(this.get("extension"),"change:loadable change:loadError change:enabled",()=>{this._updateItemState(),this._updateActions()})},_updateActions(){var e,t=this.get("extension"),i=[];t.get("loadable")?t.get("enabled")?(e=t.get("configURL"),(t=t.get("dbURL"))&&i.push({id:"database",label:gettext("Database"),url:t}),e&&i.push({id:"configure",label:gettext("Configure"),primary:!0,url:e}),i.push({danger:!0,id:"disable",label:gettext("Disable")})):i.push({id:"enable",label:gettext("Enable"),primary:!0}):i.push({id:"reload",label:gettext("Reload")}),this.setActions(i)},_updateItemState(){var e=this.get("extension");let t;t=e.get("loadable")?e.get("enabled")?"enabled":"disabled":"error",this.set("itemState",t)}}),t=Djblets.Config.TableItemView.extend({className:"djblets-c-extension-item djblets-c-config-forms-list__item",actionHandlers:{disable:"_onDisableClicked",enable:"_onEnableClicked",reload:"_onReloadClicked"},template:_.template(`<td class="djblets-c-config-forms-list__item-main">
 <div class="djblets-c-extension-item__header">
  <h3 class="djblets-c-extension-item__name"><%- name %></h3>
  <span class="djblets-c-extension-item__version"><%- version %></span>
  <div class="djblets-c-extension-item__author">
   <% if (authorURL) { %>
    <a href="<%- authorURL %>"><%- author %></a>
   <% } else { %>
    <%- author %>
   <% } %>
  </div>
 </div>
 <p class="djblets-c-extension-item__description">
  <%- summary %>
 </p>
 <% if (!loadable) { %>
  <pre class="djblets-c-extension-item__load-error"><%-
    loadError %></pre>
 <% } %>
</td>
<td class="djblets-c-config-forms-list__item-state"></td>
<td></td>`),getRenderContext(){return this.model.get("extension").attributes},_onDisableClicked(){return this.model.get("extension").disable().catch(e=>{alert(interpolate(gettext("Failed to disable the extension: %(value1)s."),{value1:e.message},!0))})},_onEnableClicked(){return this.model.get("extension").enable().catch(e=>{alert(interpolate(gettext("Failed to enable the extension: %(value1)s."),{value1:e.message},!0))})},_onReloadClicked(){return new Promise(()=>this.model.trigger("needsReload"))}}),Djblets.ExtensionManagerView=Backbone.View.extend({events:{"click .djblets-c-extensions__reload":"_reloadFull"},listItemType:e,listItemViewType:t,listItemsCollectionType:Djblets.Config.ListItems,listViewType:Djblets.Config.TableView,initialize(){this.list=new Djblets.Config.List({},{collection:new this.listItemsCollectionType([],{model:this.listItemType})})},render(){var e=this.model;const t=this.list;return this.listView=new this.listViewType({ItemView:this.listItemViewType,el:this.$(".djblets-c-config-forms-list"),model:t}),this.listView.render().$el.removeAttr("aria-busy").addClass("-all-items-are-multiline"),this._$listContainer=this.listView.$el.parent(),this.listenTo(e,"loading",()=>t.collection.reset()),this.listenTo(e,"loaded",this._onLoaded),e.load(),this},_onLoaded(){const t=this.list.collection;this.model.installedExtensions.each(e=>{e=t.add({extension:e});this.listenTo(e,"needsReload",this._reloadFull)})},_reloadFull(){this.el.submit()}})}.call(this);
