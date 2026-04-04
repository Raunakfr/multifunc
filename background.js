var state = "False";
const fileUrl = "file:///D:/Downloads/LI%20HOMIE/state.txt";
async function studymodechecker(){
    const studystate = await fetch(fileUrl);
    var statet = studystate.text();
    return statet;
}
chrome.storage.local.set({"studymode":false});
const alloweddomains=["chrome://extensions","chrome://newtab","unstop", "youtube", "google", "chatgpt.com", "gmail", "studytogether", "gemini", "napkin", "classroom", "canva", "drive", "github", "lovable", "leetcode", "linkedin", "meet", "maps", "namespace", "onlinegdb", "office"]
chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {
    if(changeInfo.url){
        const mode = await studymodechecker();
        console.log(mode)
        console.log(`Tab ${tabId} redirected to ${changeInfo.url}`);
        if(mode=="True"){
                for(const domain of alloweddomains){
                state = "False";
                if(changeInfo.url.includes(domain)){
                    console.log("")
                    state = "True";
                    break;
                }
            }
            if(state == "False"){
                chrome.notifications.create(`notif_id_${Date.now()}`,{
                    type: "basic",
                    iconUrl: "icon1.png",
                    title: "Focus!!!",
                    message: "Focus on your studies, this tab will close in 5 seconds. If this is a mistake, kindly contact the developer",
                    priority: 2
                });
                chrome.tts.speak("Focus child..... or you shall fail in what you're doing",{'pitch': 1}, {'rate': 0.5})
                setTimeout(() => {
                    chrome.tabs.remove(tabId)
                }, 5000);
            }
            if(changeInfo.url.split("/").includes("www.youtube.com") && changeInfo.url.split("/").includes("shorts")){
                chrome.tabs.remove(tabId);
            }
        }
        else{
            console.log("Study mode not active, ignoring")
        }
        
}
} );