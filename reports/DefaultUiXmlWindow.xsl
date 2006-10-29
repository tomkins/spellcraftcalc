<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output encoding="iso-8859-1" method="xml" indent="yes"/>
<xsl:template name="formatCost">
	<xsl:param name="cost"/>
	<xsl:variable name="plat" select="floor($cost div 10000000)"/>
	<xsl:variable name="gold" select="floor(($cost - $plat * 10000000) div 10000)"/>
	<xsl:variable name="silver" select="floor(($cost - $plat * 10000000 - $gold * 10000) div 100)"/>
	<xsl:variable name="copper" select="floor(($cost - $plat * 10000000 - $gold * 10000 - $silver * 100))"/>
	<xsl:if test="$plat &gt; 0"><xsl:copy-of select="$plat"/>p </xsl:if>
	<xsl:if test="$gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$gold"/>g </xsl:if>
	<xsl:if test="$silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$silver"/>s </xsl:if>
	<xsl:if test="$copper &gt; 0 or $silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$copper"/>c</xsl:if>
</xsl:template>

<xsl:template name="labeldef">
    <xsl:param name="uiwidth"/>
    <xsl:param name="uiposx"/>
    <xsl:param name="uiposy"/>
    <xsl:param name="uidata"/>
<LabelDef>
    <Color>
            <R>255</R>
            <G>255</G>
            <B>255</B>
            <A>255</A>
    </Color>
    <FontName>arial9</FontName>
    <xsl:choose>
    <xsl:when test="number($uiwidth) = -1">
    <Width><xsl:value-of select="string-length($uidata) * 15"/></Width>
    </xsl:when>
    <xsl:otherwise>
    <Width><xsl:copy-of select="$uiwidth"/></Width>
    </xsl:otherwise>
    </xsl:choose>
    <Height>16</Height>
    <MaxCharacters><xsl:value-of select="string-length($uidata) + 1"/></MaxCharacters>
    <Position>
            <X><xsl:copy-of select="$uiposx"/></X>
            <Y>-----</Y>
    </Position>
    <Data><xsl:copy-of select="uidata"/></Data>
</LabelDef>
</xsl:template>

<xsl:template match="/SCTemplate">
<Root_Element ID="DAOCUi">
	<WindowTemplate>

<label width="-1" x="5"><data>Config Report</data></label>
<empty/>
<label width="-1" x="5"><data>Stats</data></label>
<xsl:for-each select="Stats/*">
	<xsl:if test="name() != 'AF' and name() != 'PowerPool'">
	<xsl:if test="position() mod 3 = 1"><xsl:text disable-output-escaping="yes">&lt;label width="-1" x="5"&gt;&lt;data&gt;</xsl:text></xsl:if>
	<xsl:value-of select="substring(name(),1,3)"/>: <xsl:value-of select="TotalBonus"/> / <xsl:value-of select="BaseCap"/><xsl:text> </xsl:text>
	<xsl:if test="position() mod 3 = 0 or position() = last() - 2"><xsl:text disable-output-escaping="yes">&lt;/data&gt;&lt;/label&gt;</xsl:text>
	</xsl:if>
	</xsl:if>
</xsl:for-each>
<empty/>
<label width="-1" x="5"><data>Resists</data></label>
<xsl:for-each select="Resists/*">
	<xsl:if test="position() mod 3 = 1"><xsl:text disable-output-escaping="yes">&lt;label width="-1" x="5"&gt;&lt;data&gt;</xsl:text></xsl:if>
	<xsl:value-of select="name()"/>: <xsl:value-of select="TotalBonus"/> / <xsl:value-of select="BaseCap"/><xsl:text> </xsl:text>
	<xsl:if test="position() mod 3 = 0 or position() = last()"><xsl:text disable-output-escaping="yes">&lt;/data&gt;&lt;/label&gt;</xsl:text>
	</xsl:if>
</xsl:for-each>
<!--
<center><b>Skills</b></center><hr />


<skills/><br />
<center><b>Focus</b></center><hr />
<foci/><br />
<center><b>Cap Increases</b></center><hr />
<capbonuses/><br />
<center><b>Other Bonuses</b></center><hr />
<otherbonuses/><br />
-->

<empty/>
<label x="5" width="-1"><data>Piece Listing</data></label>
<xsl:for-each select="SCItem">
	<xsl:if test="count(SLOT) &gt; 0 and Equipped = '1'">
		<label width="-1" x="5"><data><xsl:value-of select="Location" /></data></label>
		<xsl:choose>
			<xsl:when test="ActiveState = 'drop'">
				<label width="-1" x="5"><data>Name: <xsl:value-of select="Name"/></data></label>
				<label width="-1" x="5">
                    <data>Level: <xsl:value-of select="Level"/> Quality: <xsl:value-of select="ItemQuality"/></data>
                </label>
				<label width="-1" x="5">
                    <data>AF/DPS: <xsl:value-of select="AFDPS"/> Bonus: <xsl:value-of select="Bonus"/></data>
                </label>
			</xsl:when>
			<xsl:otherwise>
				<label width="-1" x="5">
					<data>Imbue Points: <xsl:value-of select="format-number(sum(SLOT/Imbue), '##.0')"/> 
					<xsl:text> </xsl:text>of <xsl:value-of select="format-number(ItemImbue, '##.0')"/> 
					<xsl:text> </xsl:text>Quality: <xsl:value-of select="ItemQuality"/> Overcharge: <xsl:value-of select="Overcharge"/></data>
                </label>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:for-each select="SLOT">
			<xsl:variable name="slotnum">
				<xsl:value-of select="number(@Number) + 1"/>
			</xsl:variable>
			<xsl:if test="Type != 'Unused'">
				<xsl:choose>
					<xsl:when test="number(@Number) &lt;= 4 and ../ActiveState = 'player'">
                        <label width="-1" x="5">
                            <data>Gem <xsl:copy-of select="$slotnum"/>: <xsl:value-of select="Amount" />
                                <xsl:text> </xsl:text><xsl:value-of select="Effect" /> - <xsl:value-of select="Qua"/>
                                <xsl:text> </xsl:text><xsl:value-of select="Name"/></data>
                        </label>
					</xsl:when>
					<xsl:otherwise>
                        <label width="-1" x="5">
                            <data>Effect <xsl:copy-of select="$slotnum"/>: <xsl:value-of select="Amount"/><xsl:text> </xsl:text><xsl:value-of select="Effect"/>
						<xsl:if test="../ActiveState = 'player'">
							<xsl:text> </xsl:text>- <xsl:value-of select="Name"/>
						</xsl:if>
						</data></label>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:if>
		</xsl:for-each>
		<label width="-1" x="5"><data>Utility: <xsl:value-of select="Utility"/></data></label>
		<xsl:if test="ActiveState = 'player'">
            <label width="-1" x="5">
                <data>Cost: <xsl:call-template name="formatCost"><xsl:with-param name="cost" select="Cost"/></xsl:call-template></data>
            </label>
		</xsl:if>
	</xsl:if>
</xsl:for-each>

	</WindowTemplate>
</Root_Element>
</xsl:template>
</xsl:stylesheet>
