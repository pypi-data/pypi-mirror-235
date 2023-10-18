/* Javascript for H5PPlayerXBlock. */
function H5PPlayerXBlock(runtime, element, args) {

    if (!window.H5PPlayerXBlockPromises) {
        window.H5PPlayerXBlockPromises = [];
    }
    const contentUserDataUrl = runtime.handlerUrl(element, 'user_interaction_data');
    const contentxResultSaveUrl = runtime.handlerUrl(element, 'result_handler');

    const playerPromise = function edXH5PPlayer(el) {
        if (el && $(el).children('.h5p-iframe-wrapper').length == 0) {
            const userObj = { 'name': args.user_full_name, 'mail': args.user_email };
            const options = {
                h5pJsonPath: args.h5pJsonPath,
                frameJs: 'https://cdn.jsdelivr.net/npm/h5p-standalone@3.6.0/dist/frame.bundle.js',
                frameCss: 'https://cdn.jsdelivr.net/npm/h5p-standalone@3.6.0/dist/styles/h5p.css',
                frame: args.frame,
                copyright: args.copyright,
                icon: args.icon,
                fullScreen: args.fullScreen,
                user: userObj,
                saveFreq: args.saveFreq,
                customJs: args.customJsPath,
                contentUserData: [{
                    state: args.userData
                }],
                ajax: { 
                    contentUserDataUrl: contentUserDataUrl
                }
            }

            return new H5PStandalone.H5P(el, options).then(function(){ 
                $(el).siblings('.spinner-container').find('.spinner-border').hide();
                $(el).show();        
                H5P.externalDispatcher.on("xAPI", (event) => {

                    let hasStatement = event && event.data && event.data.statement;
                    if (!hasStatement) {
                        return;
                    }
        
                    let statement = event.data.statement;
                    let validVerb = statement.verb && statement.verb.display && statement.verb.display['en-US'];
                    if (!validVerb) {
                        return;
                    }
        
                    let isCompleted = statement.verb.display['en-US'] === 'answered' ||
                        statement.verb.display['en-US'] === 'completed';
                        let isChild = statement.context && statement.context.contextActivities &&
                        statement.context.contextActivities.parent &&
                        statement.context.contextActivities.parent[0] &&
                        statement.context.contextActivities.parent[0].id;
        
                    // Store only completed root events.
                    if (isCompleted && !isChild) {
                        $.ajax({
                            type: "POST",
                            url: contentxResultSaveUrl,
                            data: JSON.stringify(event.data.statement)
                        });    
                    }
                    // uncomment to see all xAPI events triggered by H5P content
                    //console.log("xAPI event: ", event);
                });
    
            });
        }
    };

    const h5pel = document.getElementById('h5p-' + args.player_id);
    window.H5PPlayerXBlockPromises.push(playerPromise(h5pel));
    window.H5PXBlockPlayersInitlized = false;

    $(function ($) {
        if (!H5PXBlockPlayersInitlized) {
            window.H5PXBlockPlayersInitlized = true;
            window.H5PPlayerXBlockPromises.reduce(
                function(prevPromise, curPromise) {
                    return prevPromise.then(curPromise);
                }, Promise.resolve()
            );
        }
    });
}
