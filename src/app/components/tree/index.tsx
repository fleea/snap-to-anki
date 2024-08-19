import {TreeViewProps} from "@/app/components/tree/tree";
import TreeItem from "@/app/components/tree/item";

const Tree = ({data}: TreeViewProps) => {
    return (
        <div
            className="hs-accordion-treeview-root"
            role="tree"
            aria-orientation="vertical"
        >
            <div
                className="hs-accordion-group"
                role="group"
                data-hs-accordion-always-open=""
            >
                {data.map((d) => <TreeItem key={d.id} data={d}/>)}
            </div>
        </div>
    );
};

export default Tree;