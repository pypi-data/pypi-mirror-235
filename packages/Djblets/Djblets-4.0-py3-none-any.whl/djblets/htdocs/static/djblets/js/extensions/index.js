(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
  typeof define === 'function' && define.amd ? define(['exports'], factory) :
  (global = typeof globalThis !== 'undefined' ? globalThis : global || self, factory(global.Djblets = global.Djblets || {}));
})(this, (function (exports) { 'use strict';

  function _defineProperty(obj, key, value) {
    if (key in obj) {
      Object.defineProperty(obj, key, {
        value: value,
        enumerable: true,
        configurable: true,
        writable: true
      });
    } else {
      obj[key] = value;
    }
    return obj;
  }

  var _class$3, _class2$2;
  /**
   * Base class for an extension.
   */


  /**
   * Base class for an extension.
   *
   * Extensions that deal with JavaScript should subclass this to provide any
   * initialization code it needs, such as the initialization of hooks.
   *
   * Extension instances will have read access to the server-stored settings
   * for the extension.
   */
  let Extension = Spina.spina(_class$3 = (_class2$2 = class Extension extends Spina.BaseModel {
    /**
     * Initialize the extension.
     *
     * Subclasses that override this are expected to call this method.
     */
    initialize() {
      this.hooks = [];
    }
  }, _defineProperty(_class2$2, "defaults", {
    id: null,
    name: null,
    settings: {}
  }), _class2$2)) || _class$3;

  var _dec, _class$2, _class2$1;
  /**
   * Base support for defining extension hooks.
   */


  /**
   * Base class for hooks that an extension can use to augment functionality.
   *
   * Each type of hook represents a point in the codebase that an extension
   * is able to plug functionality into.
   *
   * Subclasses are expected to set a hookPoint field in the prototype to an
   * instance of ExtensionPoint.
   *
   * Instances of an ExtensionHook subclass that extensions create will be
   * automatically registered with both the extension and the list of hooks
   * for that ExtensionHook subclass.
   *
   * Callers that use ExtensionHook subclasses to provide functionality can
   * use the subclass's each() method to loop over all registered hooks.
   */
  let ExtensionHook = (_dec = Spina.spina({
    prototypeAttrs: ['each', 'hookPoint']
  }), _dec(_class$2 = (_class2$1 = class ExtensionHook extends Spina.BaseModel {
    /**
     * An ExtensionHookPoint instance.
     *
     * This must be defined and instantiated by a subclass of ExtensionHook,
     * but not by subclasses created by extensions.
     */

    /**
     * Loop through each registered hook instance and call the given callback.
     *
     * Args:
     *     cb (function):
     *         The callback to call.
     *
     *     context (object, optional):
     *         Optional context to use when calling the callback.
     */
    static each(cb) {
      let context = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : null;
      for (const hook of this.prototype.hookPoint.hooks) {
        cb.call(context, hook);
      }
    }

    /**
     * Initialize the hook.
     *
     * This will add the instance of the hook to the extension's list of
     * hooks, and to the list of known hook instances for this hook point.
     *
     * After initialization, setUpHook will be called, which a subclass
     * can use to provide additional setup.
     */
    initialize() {
      const extension = this.get('extension');
      console.assert(!!this.hookPoint, 'This ExtensionHook subclass must define hookPoint');
      console.assert(!!extension, 'An Extension instance must be passed to ExtensionHook');
      extension.hooks.push(this);
      this.hookPoint.addHook(this);
      this.setUpHook();
    }

    /**
     * Set up additional state for the hook.
     *
     * This can be overridden by subclasses to provide additional
     * functionality.
     */
    setUpHook() {
      /* Empty by default. */
    }
  }, _defineProperty(_class2$1, "hookPoint", null), _defineProperty(_class2$1, "defaults", {
    extension: null
  }), _class2$1)) || _class$2);

  var _class$1;
  /**
   * Class for defining a hook point for extension hooks.
   */


  /**
   * Defines a point where extension hooks can plug into.
   *
   * This is meant to be instantiated and provided as a 'hookPoint' field on
   * an ExtensionHook subclass, in order to provide a place to hook into.
   */
  let ExtensionHookPoint = Spina.spina(_class$1 = class ExtensionHookPoint extends Spina.BaseModel {
    /**********************
     * Instance variables *
     **********************/

    /**
     * A list of all hooks registered on this extension point.
     */

    /**
     * Initialize the hook point.
     */
    initialize() {
      this.hooks = [];
    }

    /**
     * Add a hook instance to the list of known hooks.
     *
     * Args:
     *     hook (Djblets.ExtensionHook):
     *         The hook instance.
     */
    addHook(hook) {
      this.hooks.push(hook);
    }
  }) || _class$1;

  var _class, _class2, _class3, _class4, _class5, _class6;
  /**
   * Extension management support.
   */





  /**
   * Attributes for information on an installed extension.
   *
   * Version Added:
   *     4.0
   */
  /**
   * Represents an installed extension listed in the Manage Extensions list.
   *
   * This stores the various information about the extension that we'll display
   * to the user, and offers actions for enabling or disabling the extension.
   */
  let InstalledExtension = Spina.spina(_class = (_class2 = class InstalledExtension extends Spina.BaseModel {
    /**
     * Enable the extension.
     *
     * This will submit a request to the server to enable this extension.
     *
     * Returns:
     *     Promise:
     *     A promise that will be resolved when the request to enable the
     *     extension completes.
     */
    enable() {
      return new Promise((resolve, reject) => {
        this.save({
          enabled: true
        }, {
          wait: true,
          error: (model, xhr) => {
            this.set({
              canEnable: !xhr.errorRsp.needs_reload,
              loadError: xhr.errorRsp.load_error,
              loadable: false
            });
            reject(new Error(xhr.errorText));
          },
          success: () => resolve()
        });
      });
    }

    /**
     * Disable the extension.
     *
     * This will submit a request to the server to disable this extension.
     *
     * Returns:
     *     Promise:
     *     A promise that will be resolved when the request to enable the
     *     extension completes.
     */
    disable() {
      return new Promise((resolve, reject) => {
        this.save({
          enabled: false
        }, {
          wait: true,
          error: xhr => reject(new Error(xhr.errorText)),
          success: () => resolve()
        });
      });
    }

    /**
     * Return a JSON payload for requests sent to the server.
     *
     * Returns:
     *     object:
     *     A payload that will be serialized for making the API request.
     */
    toJSON() {
      return {
        enabled: this.get('enabled')
      };
    }

    /**
     * Parse a JSON payload from the server.
     *
     * Args:
     *     rsp (object):
     *         The payload from the server.
     *
     * Returns:
     *     object:
     *     The parsed response.
     */
    parse(rsp) {
      if (rsp.stat !== undefined) {
        rsp = rsp.extension;
      }
      const id = rsp.class_name;
      const configLink = rsp.links['admin-configure'];
      const dbLink = rsp.links['admin-database'];
      this.url = `${this.collection.url}${id}/`;
      return {
        author: rsp.author,
        authorURL: rsp.author_url,
        canDisable: rsp.can_disable,
        canEnable: rsp.can_enable,
        configURL: configLink ? configLink.href : null,
        dbURL: dbLink ? dbLink.href : null,
        enabled: rsp.enabled,
        id: id,
        loadError: rsp.load_error,
        loadable: rsp.loadable,
        name: rsp.name,
        summary: rsp.summary,
        version: rsp.version
      };
    }

    /**
     * Perform AJAX requests against the server-side API.
     *
     * Args:
     *     method (string):
     *         The HTTP method to use.
     *
     *     model (InstalledExtension):
     *         The extension object being synced.
     *
     *     options (object):
     *         Options for the sync operation.
     */
    sync(method, model, options) {
      return Backbone.sync.call(this, method, model, _.defaults({
        contentType: 'application/x-www-form-urlencoded',
        data: model.toJSON(),
        processData: true,
        error: (xhr, textStatus, errorThrown) => {
          let rsp;
          let text;
          try {
            rsp = $.parseJSON(xhr.responseText);
            text = rsp.err.msg;
          } catch (e) {
            text = 'HTTP ' + xhr.status + ' ' + xhr.statusText;
            rsp = {
              canEnable: false,
              loadError: text
            };
          }
          if (_.isFunction(options.error)) {
            xhr.errorText = text;
            xhr.errorRsp = rsp;
            options.error(xhr, textStatus, errorThrown);
          }
        }
      }, options));
    }
  }, _defineProperty(_class2, "defaults", {
    author: null,
    authorURL: null,
    configURL: null,
    dbURL: null,
    enabled: false,
    loadError: null,
    loadable: true,
    name: null,
    summary: null,
    version: null
  }), _class2)) || _class;
  /**
   * A collection of installed extensions.
   *
   * This stores the list of installed extensions, and allows fetching from
   * the API.
   */
  let InstalledExtensionCollection = Spina.spina(_class3 = (_class4 = class InstalledExtensionCollection extends Spina.BaseCollection {
    /**
     * Parse the response from the server.
     *
     * Args:
     *     rsp (object):
     *         The response from the server.
     *
     * Returns:
     *     object:
     *     The parsed data from the response.
     */
    parse(rsp) {
      return rsp.extensions;
    }
  }, _defineProperty(_class4, "model", InstalledExtension), _class4)) || _class3;
  /**
   * Manages installed extensions.
   *
   * This stores a collection of installed extensions, and provides
   * functionality for loading the current list from the server.
   */
  let ExtensionManager = Spina.spina(_class5 = (_class6 = class ExtensionManager extends Spina.BaseModel {
    /**
     * Initialize the manager.
     */
    initialize() {
      this.installedExtensions = new InstalledExtensionCollection();
      this.installedExtensions.url = this.get('apiRoot');
    }

    /**
     * Load the extensions list.
     */
    load() {
      this.trigger('loading');
      this.installedExtensions.fetch({
        success: () => this.trigger('loaded')
      });
    }
  }, _defineProperty(_class6, "defaults", {
    apiRoot: null
  }), _class6)) || _class5;

  exports.Extension = Extension;
  exports.ExtensionHook = ExtensionHook;
  exports.ExtensionHookPoint = ExtensionHookPoint;
  exports.ExtensionManager = ExtensionManager;

}));
//# sourceMappingURL=index.js.map
